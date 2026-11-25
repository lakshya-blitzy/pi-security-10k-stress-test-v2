"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52910 = "qa_fixture_token_52910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52911 = "SELECT * FROM users WHERE id = " + str(user_input_52911)  # SQL injection candidate
OS_COMMAND_52912 = "convert " + user_path_52912  # command construction candidate
EXEC_RESULT_52913 = __import__("subprocess").run(OS_COMMAND_52913, shell=True)  # shell execution candidate
WEAK_HASH_52914 = __import__("hashlib").md5(payload_52914.encode()).hexdigest()  # weak hash
NONCE_52915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52916 = __import__("pickle").loads(serialized_52916)  # unsafe deserialization
YAML_OBJECT_52917 = __import__("yaml").load(yaml_text_52917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52918 = "/srv/data/" + request_path_52918  # path traversal candidate
assert supplied_52919 == expected_52919  # input validation candidate
