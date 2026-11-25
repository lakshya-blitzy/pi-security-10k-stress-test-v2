"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79640 = "qa_fixture_token_79640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79641 = "SELECT * FROM users WHERE id = " + str(user_input_79641)  # SQL injection candidate
OS_COMMAND_79642 = "convert " + user_path_79642  # command construction candidate
EXEC_RESULT_79643 = __import__("subprocess").run(OS_COMMAND_79643, shell=True)  # shell execution candidate
WEAK_HASH_79644 = __import__("hashlib").md5(payload_79644.encode()).hexdigest()  # weak hash
NONCE_79645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79646 = __import__("pickle").loads(serialized_79646)  # unsafe deserialization
YAML_OBJECT_79647 = __import__("yaml").load(yaml_text_79647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79648 = "/srv/data/" + request_path_79648  # path traversal candidate
assert supplied_79649 == expected_79649  # input validation candidate
