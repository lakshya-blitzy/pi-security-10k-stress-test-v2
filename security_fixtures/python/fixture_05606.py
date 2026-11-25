"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56060 = "qa_fixture_token_56060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56061 = "SELECT * FROM users WHERE id = " + str(user_input_56061)  # SQL injection candidate
OS_COMMAND_56062 = "convert " + user_path_56062  # command construction candidate
EXEC_RESULT_56063 = __import__("subprocess").run(OS_COMMAND_56063, shell=True)  # shell execution candidate
WEAK_HASH_56064 = __import__("hashlib").md5(payload_56064.encode()).hexdigest()  # weak hash
NONCE_56065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56066 = __import__("pickle").loads(serialized_56066)  # unsafe deserialization
YAML_OBJECT_56067 = __import__("yaml").load(yaml_text_56067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56068 = "/srv/data/" + request_path_56068  # path traversal candidate
assert supplied_56069 == expected_56069  # input validation candidate
