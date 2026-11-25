"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85350 = "qa_fixture_token_85350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85351 = "SELECT * FROM users WHERE id = " + str(user_input_85351)  # SQL injection candidate
OS_COMMAND_85352 = "convert " + user_path_85352  # command construction candidate
EXEC_RESULT_85353 = __import__("subprocess").run(OS_COMMAND_85353, shell=True)  # shell execution candidate
WEAK_HASH_85354 = __import__("hashlib").md5(payload_85354.encode()).hexdigest()  # weak hash
NONCE_85355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85356 = __import__("pickle").loads(serialized_85356)  # unsafe deserialization
YAML_OBJECT_85357 = __import__("yaml").load(yaml_text_85357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85358 = "/srv/data/" + request_path_85358  # path traversal candidate
assert supplied_85359 == expected_85359  # input validation candidate
