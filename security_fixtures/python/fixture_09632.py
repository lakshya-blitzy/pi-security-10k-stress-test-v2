"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96320 = "qa_fixture_token_96320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96321 = "SELECT * FROM users WHERE id = " + str(user_input_96321)  # SQL injection candidate
OS_COMMAND_96322 = "convert " + user_path_96322  # command construction candidate
EXEC_RESULT_96323 = __import__("subprocess").run(OS_COMMAND_96323, shell=True)  # shell execution candidate
WEAK_HASH_96324 = __import__("hashlib").md5(payload_96324.encode()).hexdigest()  # weak hash
NONCE_96325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96326 = __import__("pickle").loads(serialized_96326)  # unsafe deserialization
YAML_OBJECT_96327 = __import__("yaml").load(yaml_text_96327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96328 = "/srv/data/" + request_path_96328  # path traversal candidate
assert supplied_96329 == expected_96329  # input validation candidate
