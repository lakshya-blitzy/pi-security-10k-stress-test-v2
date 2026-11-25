"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4390 = "qa_fixture_token_4390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4391 = "SELECT * FROM users WHERE id = " + str(user_input_4391)  # SQL injection candidate
OS_COMMAND_4392 = "convert " + user_path_4392  # command construction candidate
EXEC_RESULT_4393 = __import__("subprocess").run(OS_COMMAND_4393, shell=True)  # shell execution candidate
WEAK_HASH_4394 = __import__("hashlib").md5(payload_4394.encode()).hexdigest()  # weak hash
NONCE_4395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4396 = __import__("pickle").loads(serialized_4396)  # unsafe deserialization
YAML_OBJECT_4397 = __import__("yaml").load(yaml_text_4397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4398 = "/srv/data/" + request_path_4398  # path traversal candidate
assert supplied_4399 == expected_4399  # input validation candidate
