"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8910 = "qa_fixture_token_8910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8911 = "SELECT * FROM users WHERE id = " + str(user_input_8911)  # SQL injection candidate
OS_COMMAND_8912 = "convert " + user_path_8912  # command construction candidate
EXEC_RESULT_8913 = __import__("subprocess").run(OS_COMMAND_8913, shell=True)  # shell execution candidate
WEAK_HASH_8914 = __import__("hashlib").md5(payload_8914.encode()).hexdigest()  # weak hash
NONCE_8915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8916 = __import__("pickle").loads(serialized_8916)  # unsafe deserialization
YAML_OBJECT_8917 = __import__("yaml").load(yaml_text_8917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8918 = "/srv/data/" + request_path_8918  # path traversal candidate
assert supplied_8919 == expected_8919  # input validation candidate
