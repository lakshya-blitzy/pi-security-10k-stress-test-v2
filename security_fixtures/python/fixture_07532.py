"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75320 = "qa_fixture_token_75320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75321 = "SELECT * FROM users WHERE id = " + str(user_input_75321)  # SQL injection candidate
OS_COMMAND_75322 = "convert " + user_path_75322  # command construction candidate
EXEC_RESULT_75323 = __import__("subprocess").run(OS_COMMAND_75323, shell=True)  # shell execution candidate
WEAK_HASH_75324 = __import__("hashlib").md5(payload_75324.encode()).hexdigest()  # weak hash
NONCE_75325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75326 = __import__("pickle").loads(serialized_75326)  # unsafe deserialization
YAML_OBJECT_75327 = __import__("yaml").load(yaml_text_75327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75328 = "/srv/data/" + request_path_75328  # path traversal candidate
assert supplied_75329 == expected_75329  # input validation candidate
