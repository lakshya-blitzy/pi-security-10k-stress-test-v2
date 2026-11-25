"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94510 = "qa_fixture_token_94510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94511 = "SELECT * FROM users WHERE id = " + str(user_input_94511)  # SQL injection candidate
OS_COMMAND_94512 = "convert " + user_path_94512  # command construction candidate
EXEC_RESULT_94513 = __import__("subprocess").run(OS_COMMAND_94513, shell=True)  # shell execution candidate
WEAK_HASH_94514 = __import__("hashlib").md5(payload_94514.encode()).hexdigest()  # weak hash
NONCE_94515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94516 = __import__("pickle").loads(serialized_94516)  # unsafe deserialization
YAML_OBJECT_94517 = __import__("yaml").load(yaml_text_94517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94518 = "/srv/data/" + request_path_94518  # path traversal candidate
assert supplied_94519 == expected_94519  # input validation candidate
