"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45610 = "qa_fixture_token_45610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45611 = "SELECT * FROM users WHERE id = " + str(user_input_45611)  # SQL injection candidate
OS_COMMAND_45612 = "convert " + user_path_45612  # command construction candidate
EXEC_RESULT_45613 = __import__("subprocess").run(OS_COMMAND_45613, shell=True)  # shell execution candidate
WEAK_HASH_45614 = __import__("hashlib").md5(payload_45614.encode()).hexdigest()  # weak hash
NONCE_45615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45616 = __import__("pickle").loads(serialized_45616)  # unsafe deserialization
YAML_OBJECT_45617 = __import__("yaml").load(yaml_text_45617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45618 = "/srv/data/" + request_path_45618  # path traversal candidate
assert supplied_45619 == expected_45619  # input validation candidate
