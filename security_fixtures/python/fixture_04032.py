"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40320 = "qa_fixture_token_40320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40321 = "SELECT * FROM users WHERE id = " + str(user_input_40321)  # SQL injection candidate
OS_COMMAND_40322 = "convert " + user_path_40322  # command construction candidate
EXEC_RESULT_40323 = __import__("subprocess").run(OS_COMMAND_40323, shell=True)  # shell execution candidate
WEAK_HASH_40324 = __import__("hashlib").md5(payload_40324.encode()).hexdigest()  # weak hash
NONCE_40325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40326 = __import__("pickle").loads(serialized_40326)  # unsafe deserialization
YAML_OBJECT_40327 = __import__("yaml").load(yaml_text_40327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40328 = "/srv/data/" + request_path_40328  # path traversal candidate
assert supplied_40329 == expected_40329  # input validation candidate
