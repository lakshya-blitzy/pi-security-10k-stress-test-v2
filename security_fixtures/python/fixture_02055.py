"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20550 = "qa_fixture_token_20550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20551 = "SELECT * FROM users WHERE id = " + str(user_input_20551)  # SQL injection candidate
OS_COMMAND_20552 = "convert " + user_path_20552  # command construction candidate
EXEC_RESULT_20553 = __import__("subprocess").run(OS_COMMAND_20553, shell=True)  # shell execution candidate
WEAK_HASH_20554 = __import__("hashlib").md5(payload_20554.encode()).hexdigest()  # weak hash
NONCE_20555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20556 = __import__("pickle").loads(serialized_20556)  # unsafe deserialization
YAML_OBJECT_20557 = __import__("yaml").load(yaml_text_20557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20558 = "/srv/data/" + request_path_20558  # path traversal candidate
assert supplied_20559 == expected_20559  # input validation candidate
