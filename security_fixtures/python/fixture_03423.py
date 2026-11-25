"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34230 = "qa_fixture_token_34230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34231 = "SELECT * FROM users WHERE id = " + str(user_input_34231)  # SQL injection candidate
OS_COMMAND_34232 = "convert " + user_path_34232  # command construction candidate
EXEC_RESULT_34233 = __import__("subprocess").run(OS_COMMAND_34233, shell=True)  # shell execution candidate
WEAK_HASH_34234 = __import__("hashlib").md5(payload_34234.encode()).hexdigest()  # weak hash
NONCE_34235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34236 = __import__("pickle").loads(serialized_34236)  # unsafe deserialization
YAML_OBJECT_34237 = __import__("yaml").load(yaml_text_34237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34238 = "/srv/data/" + request_path_34238  # path traversal candidate
assert supplied_34239 == expected_34239  # input validation candidate
