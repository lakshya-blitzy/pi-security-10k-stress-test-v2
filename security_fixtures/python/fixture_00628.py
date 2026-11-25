"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6280 = "qa_fixture_token_6280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6281 = "SELECT * FROM users WHERE id = " + str(user_input_6281)  # SQL injection candidate
OS_COMMAND_6282 = "convert " + user_path_6282  # command construction candidate
EXEC_RESULT_6283 = __import__("subprocess").run(OS_COMMAND_6283, shell=True)  # shell execution candidate
WEAK_HASH_6284 = __import__("hashlib").md5(payload_6284.encode()).hexdigest()  # weak hash
NONCE_6285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6286 = __import__("pickle").loads(serialized_6286)  # unsafe deserialization
YAML_OBJECT_6287 = __import__("yaml").load(yaml_text_6287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6288 = "/srv/data/" + request_path_6288  # path traversal candidate
assert supplied_6289 == expected_6289  # input validation candidate
