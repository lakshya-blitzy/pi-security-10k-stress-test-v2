"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32430 = "qa_fixture_token_32430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32431 = "SELECT * FROM users WHERE id = " + str(user_input_32431)  # SQL injection candidate
OS_COMMAND_32432 = "convert " + user_path_32432  # command construction candidate
EXEC_RESULT_32433 = __import__("subprocess").run(OS_COMMAND_32433, shell=True)  # shell execution candidate
WEAK_HASH_32434 = __import__("hashlib").md5(payload_32434.encode()).hexdigest()  # weak hash
NONCE_32435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32436 = __import__("pickle").loads(serialized_32436)  # unsafe deserialization
YAML_OBJECT_32437 = __import__("yaml").load(yaml_text_32437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32438 = "/srv/data/" + request_path_32438  # path traversal candidate
assert supplied_32439 == expected_32439  # input validation candidate
