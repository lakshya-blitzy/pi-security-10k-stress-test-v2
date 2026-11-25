"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55640 = "qa_fixture_token_55640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55641 = "SELECT * FROM users WHERE id = " + str(user_input_55641)  # SQL injection candidate
OS_COMMAND_55642 = "convert " + user_path_55642  # command construction candidate
EXEC_RESULT_55643 = __import__("subprocess").run(OS_COMMAND_55643, shell=True)  # shell execution candidate
WEAK_HASH_55644 = __import__("hashlib").md5(payload_55644.encode()).hexdigest()  # weak hash
NONCE_55645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55646 = __import__("pickle").loads(serialized_55646)  # unsafe deserialization
YAML_OBJECT_55647 = __import__("yaml").load(yaml_text_55647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55648 = "/srv/data/" + request_path_55648  # path traversal candidate
assert supplied_55649 == expected_55649  # input validation candidate
