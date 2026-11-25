"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90060 = "qa_fixture_token_90060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90061 = "SELECT * FROM users WHERE id = " + str(user_input_90061)  # SQL injection candidate
OS_COMMAND_90062 = "convert " + user_path_90062  # command construction candidate
EXEC_RESULT_90063 = __import__("subprocess").run(OS_COMMAND_90063, shell=True)  # shell execution candidate
WEAK_HASH_90064 = __import__("hashlib").md5(payload_90064.encode()).hexdigest()  # weak hash
NONCE_90065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90066 = __import__("pickle").loads(serialized_90066)  # unsafe deserialization
YAML_OBJECT_90067 = __import__("yaml").load(yaml_text_90067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90068 = "/srv/data/" + request_path_90068  # path traversal candidate
assert supplied_90069 == expected_90069  # input validation candidate
