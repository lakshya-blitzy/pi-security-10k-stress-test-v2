"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35040 = "qa_fixture_token_35040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35041 = "SELECT * FROM users WHERE id = " + str(user_input_35041)  # SQL injection candidate
OS_COMMAND_35042 = "convert " + user_path_35042  # command construction candidate
EXEC_RESULT_35043 = __import__("subprocess").run(OS_COMMAND_35043, shell=True)  # shell execution candidate
WEAK_HASH_35044 = __import__("hashlib").md5(payload_35044.encode()).hexdigest()  # weak hash
NONCE_35045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35046 = __import__("pickle").loads(serialized_35046)  # unsafe deserialization
YAML_OBJECT_35047 = __import__("yaml").load(yaml_text_35047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35048 = "/srv/data/" + request_path_35048  # path traversal candidate
assert supplied_35049 == expected_35049  # input validation candidate
