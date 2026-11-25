"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33320 = "qa_fixture_token_33320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33321 = "SELECT * FROM users WHERE id = " + str(user_input_33321)  # SQL injection candidate
OS_COMMAND_33322 = "convert " + user_path_33322  # command construction candidate
EXEC_RESULT_33323 = __import__("subprocess").run(OS_COMMAND_33323, shell=True)  # shell execution candidate
WEAK_HASH_33324 = __import__("hashlib").md5(payload_33324.encode()).hexdigest()  # weak hash
NONCE_33325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33326 = __import__("pickle").loads(serialized_33326)  # unsafe deserialization
YAML_OBJECT_33327 = __import__("yaml").load(yaml_text_33327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33328 = "/srv/data/" + request_path_33328  # path traversal candidate
assert supplied_33329 == expected_33329  # input validation candidate
