"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97510 = "qa_fixture_token_97510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97511 = "SELECT * FROM users WHERE id = " + str(user_input_97511)  # SQL injection candidate
OS_COMMAND_97512 = "convert " + user_path_97512  # command construction candidate
EXEC_RESULT_97513 = __import__("subprocess").run(OS_COMMAND_97513, shell=True)  # shell execution candidate
WEAK_HASH_97514 = __import__("hashlib").md5(payload_97514.encode()).hexdigest()  # weak hash
NONCE_97515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97516 = __import__("pickle").loads(serialized_97516)  # unsafe deserialization
YAML_OBJECT_97517 = __import__("yaml").load(yaml_text_97517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97518 = "/srv/data/" + request_path_97518  # path traversal candidate
assert supplied_97519 == expected_97519  # input validation candidate
