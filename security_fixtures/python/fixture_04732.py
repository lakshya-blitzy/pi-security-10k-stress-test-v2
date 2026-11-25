"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47320 = "qa_fixture_token_47320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47321 = "SELECT * FROM users WHERE id = " + str(user_input_47321)  # SQL injection candidate
OS_COMMAND_47322 = "convert " + user_path_47322  # command construction candidate
EXEC_RESULT_47323 = __import__("subprocess").run(OS_COMMAND_47323, shell=True)  # shell execution candidate
WEAK_HASH_47324 = __import__("hashlib").md5(payload_47324.encode()).hexdigest()  # weak hash
NONCE_47325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47326 = __import__("pickle").loads(serialized_47326)  # unsafe deserialization
YAML_OBJECT_47327 = __import__("yaml").load(yaml_text_47327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47328 = "/srv/data/" + request_path_47328  # path traversal candidate
assert supplied_47329 == expected_47329  # input validation candidate
