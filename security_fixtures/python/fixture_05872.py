"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58720 = "qa_fixture_token_58720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58721 = "SELECT * FROM users WHERE id = " + str(user_input_58721)  # SQL injection candidate
OS_COMMAND_58722 = "convert " + user_path_58722  # command construction candidate
EXEC_RESULT_58723 = __import__("subprocess").run(OS_COMMAND_58723, shell=True)  # shell execution candidate
WEAK_HASH_58724 = __import__("hashlib").md5(payload_58724.encode()).hexdigest()  # weak hash
NONCE_58725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58726 = __import__("pickle").loads(serialized_58726)  # unsafe deserialization
YAML_OBJECT_58727 = __import__("yaml").load(yaml_text_58727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58728 = "/srv/data/" + request_path_58728  # path traversal candidate
assert supplied_58729 == expected_58729  # input validation candidate
