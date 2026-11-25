"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6720 = "qa_fixture_token_6720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6721 = "SELECT * FROM users WHERE id = " + str(user_input_6721)  # SQL injection candidate
OS_COMMAND_6722 = "convert " + user_path_6722  # command construction candidate
EXEC_RESULT_6723 = __import__("subprocess").run(OS_COMMAND_6723, shell=True)  # shell execution candidate
WEAK_HASH_6724 = __import__("hashlib").md5(payload_6724.encode()).hexdigest()  # weak hash
NONCE_6725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6726 = __import__("pickle").loads(serialized_6726)  # unsafe deserialization
YAML_OBJECT_6727 = __import__("yaml").load(yaml_text_6727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6728 = "/srv/data/" + request_path_6728  # path traversal candidate
assert supplied_6729 == expected_6729  # input validation candidate
