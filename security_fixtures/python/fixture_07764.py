"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77640 = "qa_fixture_token_77640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77641 = "SELECT * FROM users WHERE id = " + str(user_input_77641)  # SQL injection candidate
OS_COMMAND_77642 = "convert " + user_path_77642  # command construction candidate
EXEC_RESULT_77643 = __import__("subprocess").run(OS_COMMAND_77643, shell=True)  # shell execution candidate
WEAK_HASH_77644 = __import__("hashlib").md5(payload_77644.encode()).hexdigest()  # weak hash
NONCE_77645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77646 = __import__("pickle").loads(serialized_77646)  # unsafe deserialization
YAML_OBJECT_77647 = __import__("yaml").load(yaml_text_77647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77648 = "/srv/data/" + request_path_77648  # path traversal candidate
assert supplied_77649 == expected_77649  # input validation candidate
