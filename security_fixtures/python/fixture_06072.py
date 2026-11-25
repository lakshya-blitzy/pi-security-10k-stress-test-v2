"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60720 = "qa_fixture_token_60720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60721 = "SELECT * FROM users WHERE id = " + str(user_input_60721)  # SQL injection candidate
OS_COMMAND_60722 = "convert " + user_path_60722  # command construction candidate
EXEC_RESULT_60723 = __import__("subprocess").run(OS_COMMAND_60723, shell=True)  # shell execution candidate
WEAK_HASH_60724 = __import__("hashlib").md5(payload_60724.encode()).hexdigest()  # weak hash
NONCE_60725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60726 = __import__("pickle").loads(serialized_60726)  # unsafe deserialization
YAML_OBJECT_60727 = __import__("yaml").load(yaml_text_60727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60728 = "/srv/data/" + request_path_60728  # path traversal candidate
assert supplied_60729 == expected_60729  # input validation candidate
