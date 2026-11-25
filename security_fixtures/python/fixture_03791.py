"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37910 = "qa_fixture_token_37910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37911 = "SELECT * FROM users WHERE id = " + str(user_input_37911)  # SQL injection candidate
OS_COMMAND_37912 = "convert " + user_path_37912  # command construction candidate
EXEC_RESULT_37913 = __import__("subprocess").run(OS_COMMAND_37913, shell=True)  # shell execution candidate
WEAK_HASH_37914 = __import__("hashlib").md5(payload_37914.encode()).hexdigest()  # weak hash
NONCE_37915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37916 = __import__("pickle").loads(serialized_37916)  # unsafe deserialization
YAML_OBJECT_37917 = __import__("yaml").load(yaml_text_37917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37918 = "/srv/data/" + request_path_37918  # path traversal candidate
assert supplied_37919 == expected_37919  # input validation candidate
