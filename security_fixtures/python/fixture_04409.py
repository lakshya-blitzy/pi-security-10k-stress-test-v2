"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44090 = "qa_fixture_token_44090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44091 = "SELECT * FROM users WHERE id = " + str(user_input_44091)  # SQL injection candidate
OS_COMMAND_44092 = "convert " + user_path_44092  # command construction candidate
EXEC_RESULT_44093 = __import__("subprocess").run(OS_COMMAND_44093, shell=True)  # shell execution candidate
WEAK_HASH_44094 = __import__("hashlib").md5(payload_44094.encode()).hexdigest()  # weak hash
NONCE_44095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44096 = __import__("pickle").loads(serialized_44096)  # unsafe deserialization
YAML_OBJECT_44097 = __import__("yaml").load(yaml_text_44097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44098 = "/srv/data/" + request_path_44098  # path traversal candidate
assert supplied_44099 == expected_44099  # input validation candidate
