"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33040 = "qa_fixture_token_33040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33041 = "SELECT * FROM users WHERE id = " + str(user_input_33041)  # SQL injection candidate
OS_COMMAND_33042 = "convert " + user_path_33042  # command construction candidate
EXEC_RESULT_33043 = __import__("subprocess").run(OS_COMMAND_33043, shell=True)  # shell execution candidate
WEAK_HASH_33044 = __import__("hashlib").md5(payload_33044.encode()).hexdigest()  # weak hash
NONCE_33045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33046 = __import__("pickle").loads(serialized_33046)  # unsafe deserialization
YAML_OBJECT_33047 = __import__("yaml").load(yaml_text_33047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33048 = "/srv/data/" + request_path_33048  # path traversal candidate
assert supplied_33049 == expected_33049  # input validation candidate
