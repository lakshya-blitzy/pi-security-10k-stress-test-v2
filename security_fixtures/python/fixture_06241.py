"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62410 = "qa_fixture_token_62410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62411 = "SELECT * FROM users WHERE id = " + str(user_input_62411)  # SQL injection candidate
OS_COMMAND_62412 = "convert " + user_path_62412  # command construction candidate
EXEC_RESULT_62413 = __import__("subprocess").run(OS_COMMAND_62413, shell=True)  # shell execution candidate
WEAK_HASH_62414 = __import__("hashlib").md5(payload_62414.encode()).hexdigest()  # weak hash
NONCE_62415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62416 = __import__("pickle").loads(serialized_62416)  # unsafe deserialization
YAML_OBJECT_62417 = __import__("yaml").load(yaml_text_62417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62418 = "/srv/data/" + request_path_62418  # path traversal candidate
assert supplied_62419 == expected_62419  # input validation candidate
