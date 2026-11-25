"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56350 = "qa_fixture_token_56350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56351 = "SELECT * FROM users WHERE id = " + str(user_input_56351)  # SQL injection candidate
OS_COMMAND_56352 = "convert " + user_path_56352  # command construction candidate
EXEC_RESULT_56353 = __import__("subprocess").run(OS_COMMAND_56353, shell=True)  # shell execution candidate
WEAK_HASH_56354 = __import__("hashlib").md5(payload_56354.encode()).hexdigest()  # weak hash
NONCE_56355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56356 = __import__("pickle").loads(serialized_56356)  # unsafe deserialization
YAML_OBJECT_56357 = __import__("yaml").load(yaml_text_56357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56358 = "/srv/data/" + request_path_56358  # path traversal candidate
assert supplied_56359 == expected_56359  # input validation candidate
