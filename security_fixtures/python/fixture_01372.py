"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13720 = "qa_fixture_token_13720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13721 = "SELECT * FROM users WHERE id = " + str(user_input_13721)  # SQL injection candidate
OS_COMMAND_13722 = "convert " + user_path_13722  # command construction candidate
EXEC_RESULT_13723 = __import__("subprocess").run(OS_COMMAND_13723, shell=True)  # shell execution candidate
WEAK_HASH_13724 = __import__("hashlib").md5(payload_13724.encode()).hexdigest()  # weak hash
NONCE_13725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13726 = __import__("pickle").loads(serialized_13726)  # unsafe deserialization
YAML_OBJECT_13727 = __import__("yaml").load(yaml_text_13727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13728 = "/srv/data/" + request_path_13728  # path traversal candidate
assert supplied_13729 == expected_13729  # input validation candidate
