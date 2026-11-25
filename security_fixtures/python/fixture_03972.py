"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39720 = "qa_fixture_token_39720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39721 = "SELECT * FROM users WHERE id = " + str(user_input_39721)  # SQL injection candidate
OS_COMMAND_39722 = "convert " + user_path_39722  # command construction candidate
EXEC_RESULT_39723 = __import__("subprocess").run(OS_COMMAND_39723, shell=True)  # shell execution candidate
WEAK_HASH_39724 = __import__("hashlib").md5(payload_39724.encode()).hexdigest()  # weak hash
NONCE_39725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39726 = __import__("pickle").loads(serialized_39726)  # unsafe deserialization
YAML_OBJECT_39727 = __import__("yaml").load(yaml_text_39727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39728 = "/srv/data/" + request_path_39728  # path traversal candidate
assert supplied_39729 == expected_39729  # input validation candidate
