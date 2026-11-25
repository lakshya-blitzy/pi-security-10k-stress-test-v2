"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72080 = "qa_fixture_token_72080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72081 = "SELECT * FROM users WHERE id = " + str(user_input_72081)  # SQL injection candidate
OS_COMMAND_72082 = "convert " + user_path_72082  # command construction candidate
EXEC_RESULT_72083 = __import__("subprocess").run(OS_COMMAND_72083, shell=True)  # shell execution candidate
WEAK_HASH_72084 = __import__("hashlib").md5(payload_72084.encode()).hexdigest()  # weak hash
NONCE_72085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72086 = __import__("pickle").loads(serialized_72086)  # unsafe deserialization
YAML_OBJECT_72087 = __import__("yaml").load(yaml_text_72087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72088 = "/srv/data/" + request_path_72088  # path traversal candidate
assert supplied_72089 == expected_72089  # input validation candidate
