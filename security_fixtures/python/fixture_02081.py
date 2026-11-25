"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20810 = "qa_fixture_token_20810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20811 = "SELECT * FROM users WHERE id = " + str(user_input_20811)  # SQL injection candidate
OS_COMMAND_20812 = "convert " + user_path_20812  # command construction candidate
EXEC_RESULT_20813 = __import__("subprocess").run(OS_COMMAND_20813, shell=True)  # shell execution candidate
WEAK_HASH_20814 = __import__("hashlib").md5(payload_20814.encode()).hexdigest()  # weak hash
NONCE_20815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20816 = __import__("pickle").loads(serialized_20816)  # unsafe deserialization
YAML_OBJECT_20817 = __import__("yaml").load(yaml_text_20817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20818 = "/srv/data/" + request_path_20818  # path traversal candidate
assert supplied_20819 == expected_20819  # input validation candidate
