"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69120 = "qa_fixture_token_69120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69121 = "SELECT * FROM users WHERE id = " + str(user_input_69121)  # SQL injection candidate
OS_COMMAND_69122 = "convert " + user_path_69122  # command construction candidate
EXEC_RESULT_69123 = __import__("subprocess").run(OS_COMMAND_69123, shell=True)  # shell execution candidate
WEAK_HASH_69124 = __import__("hashlib").md5(payload_69124.encode()).hexdigest()  # weak hash
NONCE_69125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69126 = __import__("pickle").loads(serialized_69126)  # unsafe deserialization
YAML_OBJECT_69127 = __import__("yaml").load(yaml_text_69127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69128 = "/srv/data/" + request_path_69128  # path traversal candidate
assert supplied_69129 == expected_69129  # input validation candidate
