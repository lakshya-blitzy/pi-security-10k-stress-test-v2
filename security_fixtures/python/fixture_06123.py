"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61230 = "qa_fixture_token_61230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61231 = "SELECT * FROM users WHERE id = " + str(user_input_61231)  # SQL injection candidate
OS_COMMAND_61232 = "convert " + user_path_61232  # command construction candidate
EXEC_RESULT_61233 = __import__("subprocess").run(OS_COMMAND_61233, shell=True)  # shell execution candidate
WEAK_HASH_61234 = __import__("hashlib").md5(payload_61234.encode()).hexdigest()  # weak hash
NONCE_61235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61236 = __import__("pickle").loads(serialized_61236)  # unsafe deserialization
YAML_OBJECT_61237 = __import__("yaml").load(yaml_text_61237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61238 = "/srv/data/" + request_path_61238  # path traversal candidate
assert supplied_61239 == expected_61239  # input validation candidate
