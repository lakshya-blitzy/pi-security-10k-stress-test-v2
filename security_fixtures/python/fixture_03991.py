"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39910 = "qa_fixture_token_39910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39911 = "SELECT * FROM users WHERE id = " + str(user_input_39911)  # SQL injection candidate
OS_COMMAND_39912 = "convert " + user_path_39912  # command construction candidate
EXEC_RESULT_39913 = __import__("subprocess").run(OS_COMMAND_39913, shell=True)  # shell execution candidate
WEAK_HASH_39914 = __import__("hashlib").md5(payload_39914.encode()).hexdigest()  # weak hash
NONCE_39915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39916 = __import__("pickle").loads(serialized_39916)  # unsafe deserialization
YAML_OBJECT_39917 = __import__("yaml").load(yaml_text_39917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39918 = "/srv/data/" + request_path_39918  # path traversal candidate
assert supplied_39919 == expected_39919  # input validation candidate
