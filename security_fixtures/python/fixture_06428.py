"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64280 = "qa_fixture_token_64280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64281 = "SELECT * FROM users WHERE id = " + str(user_input_64281)  # SQL injection candidate
OS_COMMAND_64282 = "convert " + user_path_64282  # command construction candidate
EXEC_RESULT_64283 = __import__("subprocess").run(OS_COMMAND_64283, shell=True)  # shell execution candidate
WEAK_HASH_64284 = __import__("hashlib").md5(payload_64284.encode()).hexdigest()  # weak hash
NONCE_64285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64286 = __import__("pickle").loads(serialized_64286)  # unsafe deserialization
YAML_OBJECT_64287 = __import__("yaml").load(yaml_text_64287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64288 = "/srv/data/" + request_path_64288  # path traversal candidate
assert supplied_64289 == expected_64289  # input validation candidate
