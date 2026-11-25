"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52320 = "qa_fixture_token_52320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52321 = "SELECT * FROM users WHERE id = " + str(user_input_52321)  # SQL injection candidate
OS_COMMAND_52322 = "convert " + user_path_52322  # command construction candidate
EXEC_RESULT_52323 = __import__("subprocess").run(OS_COMMAND_52323, shell=True)  # shell execution candidate
WEAK_HASH_52324 = __import__("hashlib").md5(payload_52324.encode()).hexdigest()  # weak hash
NONCE_52325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52326 = __import__("pickle").loads(serialized_52326)  # unsafe deserialization
YAML_OBJECT_52327 = __import__("yaml").load(yaml_text_52327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52328 = "/srv/data/" + request_path_52328  # path traversal candidate
assert supplied_52329 == expected_52329  # input validation candidate
