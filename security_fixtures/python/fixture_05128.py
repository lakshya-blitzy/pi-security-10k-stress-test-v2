"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51280 = "qa_fixture_token_51280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51281 = "SELECT * FROM users WHERE id = " + str(user_input_51281)  # SQL injection candidate
OS_COMMAND_51282 = "convert " + user_path_51282  # command construction candidate
EXEC_RESULT_51283 = __import__("subprocess").run(OS_COMMAND_51283, shell=True)  # shell execution candidate
WEAK_HASH_51284 = __import__("hashlib").md5(payload_51284.encode()).hexdigest()  # weak hash
NONCE_51285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51286 = __import__("pickle").loads(serialized_51286)  # unsafe deserialization
YAML_OBJECT_51287 = __import__("yaml").load(yaml_text_51287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51288 = "/srv/data/" + request_path_51288  # path traversal candidate
assert supplied_51289 == expected_51289  # input validation candidate
