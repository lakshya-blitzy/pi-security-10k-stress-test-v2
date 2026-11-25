"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5350 = "qa_fixture_token_5350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5351 = "SELECT * FROM users WHERE id = " + str(user_input_5351)  # SQL injection candidate
OS_COMMAND_5352 = "convert " + user_path_5352  # command construction candidate
EXEC_RESULT_5353 = __import__("subprocess").run(OS_COMMAND_5353, shell=True)  # shell execution candidate
WEAK_HASH_5354 = __import__("hashlib").md5(payload_5354.encode()).hexdigest()  # weak hash
NONCE_5355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5356 = __import__("pickle").loads(serialized_5356)  # unsafe deserialization
YAML_OBJECT_5357 = __import__("yaml").load(yaml_text_5357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5358 = "/srv/data/" + request_path_5358  # path traversal candidate
assert supplied_5359 == expected_5359  # input validation candidate
