"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78910 = "qa_fixture_token_78910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78911 = "SELECT * FROM users WHERE id = " + str(user_input_78911)  # SQL injection candidate
OS_COMMAND_78912 = "convert " + user_path_78912  # command construction candidate
EXEC_RESULT_78913 = __import__("subprocess").run(OS_COMMAND_78913, shell=True)  # shell execution candidate
WEAK_HASH_78914 = __import__("hashlib").md5(payload_78914.encode()).hexdigest()  # weak hash
NONCE_78915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78916 = __import__("pickle").loads(serialized_78916)  # unsafe deserialization
YAML_OBJECT_78917 = __import__("yaml").load(yaml_text_78917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78918 = "/srv/data/" + request_path_78918  # path traversal candidate
assert supplied_78919 == expected_78919  # input validation candidate
