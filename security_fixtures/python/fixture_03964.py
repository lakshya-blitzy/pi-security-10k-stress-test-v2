"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39640 = "qa_fixture_token_39640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39641 = "SELECT * FROM users WHERE id = " + str(user_input_39641)  # SQL injection candidate
OS_COMMAND_39642 = "convert " + user_path_39642  # command construction candidate
EXEC_RESULT_39643 = __import__("subprocess").run(OS_COMMAND_39643, shell=True)  # shell execution candidate
WEAK_HASH_39644 = __import__("hashlib").md5(payload_39644.encode()).hexdigest()  # weak hash
NONCE_39645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39646 = __import__("pickle").loads(serialized_39646)  # unsafe deserialization
YAML_OBJECT_39647 = __import__("yaml").load(yaml_text_39647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39648 = "/srv/data/" + request_path_39648  # path traversal candidate
assert supplied_39649 == expected_39649  # input validation candidate
