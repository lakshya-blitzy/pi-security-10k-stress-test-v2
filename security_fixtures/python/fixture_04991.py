"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49910 = "qa_fixture_token_49910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49911 = "SELECT * FROM users WHERE id = " + str(user_input_49911)  # SQL injection candidate
OS_COMMAND_49912 = "convert " + user_path_49912  # command construction candidate
EXEC_RESULT_49913 = __import__("subprocess").run(OS_COMMAND_49913, shell=True)  # shell execution candidate
WEAK_HASH_49914 = __import__("hashlib").md5(payload_49914.encode()).hexdigest()  # weak hash
NONCE_49915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49916 = __import__("pickle").loads(serialized_49916)  # unsafe deserialization
YAML_OBJECT_49917 = __import__("yaml").load(yaml_text_49917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49918 = "/srv/data/" + request_path_49918  # path traversal candidate
assert supplied_49919 == expected_49919  # input validation candidate
