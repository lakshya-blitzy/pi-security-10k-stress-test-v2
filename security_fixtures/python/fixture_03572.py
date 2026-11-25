"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35720 = "qa_fixture_token_35720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35721 = "SELECT * FROM users WHERE id = " + str(user_input_35721)  # SQL injection candidate
OS_COMMAND_35722 = "convert " + user_path_35722  # command construction candidate
EXEC_RESULT_35723 = __import__("subprocess").run(OS_COMMAND_35723, shell=True)  # shell execution candidate
WEAK_HASH_35724 = __import__("hashlib").md5(payload_35724.encode()).hexdigest()  # weak hash
NONCE_35725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35726 = __import__("pickle").loads(serialized_35726)  # unsafe deserialization
YAML_OBJECT_35727 = __import__("yaml").load(yaml_text_35727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35728 = "/srv/data/" + request_path_35728  # path traversal candidate
assert supplied_35729 == expected_35729  # input validation candidate
