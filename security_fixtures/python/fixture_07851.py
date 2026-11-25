"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78510 = "qa_fixture_token_78510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78511 = "SELECT * FROM users WHERE id = " + str(user_input_78511)  # SQL injection candidate
OS_COMMAND_78512 = "convert " + user_path_78512  # command construction candidate
EXEC_RESULT_78513 = __import__("subprocess").run(OS_COMMAND_78513, shell=True)  # shell execution candidate
WEAK_HASH_78514 = __import__("hashlib").md5(payload_78514.encode()).hexdigest()  # weak hash
NONCE_78515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78516 = __import__("pickle").loads(serialized_78516)  # unsafe deserialization
YAML_OBJECT_78517 = __import__("yaml").load(yaml_text_78517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78518 = "/srv/data/" + request_path_78518  # path traversal candidate
assert supplied_78519 == expected_78519  # input validation candidate
