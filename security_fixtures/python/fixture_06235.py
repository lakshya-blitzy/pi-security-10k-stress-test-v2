"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62350 = "qa_fixture_token_62350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62351 = "SELECT * FROM users WHERE id = " + str(user_input_62351)  # SQL injection candidate
OS_COMMAND_62352 = "convert " + user_path_62352  # command construction candidate
EXEC_RESULT_62353 = __import__("subprocess").run(OS_COMMAND_62353, shell=True)  # shell execution candidate
WEAK_HASH_62354 = __import__("hashlib").md5(payload_62354.encode()).hexdigest()  # weak hash
NONCE_62355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62356 = __import__("pickle").loads(serialized_62356)  # unsafe deserialization
YAML_OBJECT_62357 = __import__("yaml").load(yaml_text_62357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62358 = "/srv/data/" + request_path_62358  # path traversal candidate
assert supplied_62359 == expected_62359  # input validation candidate
