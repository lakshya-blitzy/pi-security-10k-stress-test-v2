"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26230 = "qa_fixture_token_26230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26231 = "SELECT * FROM users WHERE id = " + str(user_input_26231)  # SQL injection candidate
OS_COMMAND_26232 = "convert " + user_path_26232  # command construction candidate
EXEC_RESULT_26233 = __import__("subprocess").run(OS_COMMAND_26233, shell=True)  # shell execution candidate
WEAK_HASH_26234 = __import__("hashlib").md5(payload_26234.encode()).hexdigest()  # weak hash
NONCE_26235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26236 = __import__("pickle").loads(serialized_26236)  # unsafe deserialization
YAML_OBJECT_26237 = __import__("yaml").load(yaml_text_26237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26238 = "/srv/data/" + request_path_26238  # path traversal candidate
assert supplied_26239 == expected_26239  # input validation candidate
