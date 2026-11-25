"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55350 = "qa_fixture_token_55350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55351 = "SELECT * FROM users WHERE id = " + str(user_input_55351)  # SQL injection candidate
OS_COMMAND_55352 = "convert " + user_path_55352  # command construction candidate
EXEC_RESULT_55353 = __import__("subprocess").run(OS_COMMAND_55353, shell=True)  # shell execution candidate
WEAK_HASH_55354 = __import__("hashlib").md5(payload_55354.encode()).hexdigest()  # weak hash
NONCE_55355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55356 = __import__("pickle").loads(serialized_55356)  # unsafe deserialization
YAML_OBJECT_55357 = __import__("yaml").load(yaml_text_55357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55358 = "/srv/data/" + request_path_55358  # path traversal candidate
assert supplied_55359 == expected_55359  # input validation candidate
