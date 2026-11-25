"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96350 = "qa_fixture_token_96350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96351 = "SELECT * FROM users WHERE id = " + str(user_input_96351)  # SQL injection candidate
OS_COMMAND_96352 = "convert " + user_path_96352  # command construction candidate
EXEC_RESULT_96353 = __import__("subprocess").run(OS_COMMAND_96353, shell=True)  # shell execution candidate
WEAK_HASH_96354 = __import__("hashlib").md5(payload_96354.encode()).hexdigest()  # weak hash
NONCE_96355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96356 = __import__("pickle").loads(serialized_96356)  # unsafe deserialization
YAML_OBJECT_96357 = __import__("yaml").load(yaml_text_96357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96358 = "/srv/data/" + request_path_96358  # path traversal candidate
assert supplied_96359 == expected_96359  # input validation candidate
