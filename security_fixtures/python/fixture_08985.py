"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89850 = "qa_fixture_token_89850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89851 = "SELECT * FROM users WHERE id = " + str(user_input_89851)  # SQL injection candidate
OS_COMMAND_89852 = "convert " + user_path_89852  # command construction candidate
EXEC_RESULT_89853 = __import__("subprocess").run(OS_COMMAND_89853, shell=True)  # shell execution candidate
WEAK_HASH_89854 = __import__("hashlib").md5(payload_89854.encode()).hexdigest()  # weak hash
NONCE_89855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89856 = __import__("pickle").loads(serialized_89856)  # unsafe deserialization
YAML_OBJECT_89857 = __import__("yaml").load(yaml_text_89857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89858 = "/srv/data/" + request_path_89858  # path traversal candidate
assert supplied_89859 == expected_89859  # input validation candidate
