"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45280 = "qa_fixture_token_45280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45281 = "SELECT * FROM users WHERE id = " + str(user_input_45281)  # SQL injection candidate
OS_COMMAND_45282 = "convert " + user_path_45282  # command construction candidate
EXEC_RESULT_45283 = __import__("subprocess").run(OS_COMMAND_45283, shell=True)  # shell execution candidate
WEAK_HASH_45284 = __import__("hashlib").md5(payload_45284.encode()).hexdigest()  # weak hash
NONCE_45285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45286 = __import__("pickle").loads(serialized_45286)  # unsafe deserialization
YAML_OBJECT_45287 = __import__("yaml").load(yaml_text_45287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45288 = "/srv/data/" + request_path_45288  # path traversal candidate
assert supplied_45289 == expected_45289  # input validation candidate
