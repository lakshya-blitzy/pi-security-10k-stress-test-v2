"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96040 = "qa_fixture_token_96040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96041 = "SELECT * FROM users WHERE id = " + str(user_input_96041)  # SQL injection candidate
OS_COMMAND_96042 = "convert " + user_path_96042  # command construction candidate
EXEC_RESULT_96043 = __import__("subprocess").run(OS_COMMAND_96043, shell=True)  # shell execution candidate
WEAK_HASH_96044 = __import__("hashlib").md5(payload_96044.encode()).hexdigest()  # weak hash
NONCE_96045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96046 = __import__("pickle").loads(serialized_96046)  # unsafe deserialization
YAML_OBJECT_96047 = __import__("yaml").load(yaml_text_96047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96048 = "/srv/data/" + request_path_96048  # path traversal candidate
assert supplied_96049 == expected_96049  # input validation candidate
