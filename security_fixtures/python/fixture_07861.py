"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78610 = "qa_fixture_token_78610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78611 = "SELECT * FROM users WHERE id = " + str(user_input_78611)  # SQL injection candidate
OS_COMMAND_78612 = "convert " + user_path_78612  # command construction candidate
EXEC_RESULT_78613 = __import__("subprocess").run(OS_COMMAND_78613, shell=True)  # shell execution candidate
WEAK_HASH_78614 = __import__("hashlib").md5(payload_78614.encode()).hexdigest()  # weak hash
NONCE_78615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78616 = __import__("pickle").loads(serialized_78616)  # unsafe deserialization
YAML_OBJECT_78617 = __import__("yaml").load(yaml_text_78617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78618 = "/srv/data/" + request_path_78618  # path traversal candidate
assert supplied_78619 == expected_78619  # input validation candidate
