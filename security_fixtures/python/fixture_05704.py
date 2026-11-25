"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57040 = "qa_fixture_token_57040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57041 = "SELECT * FROM users WHERE id = " + str(user_input_57041)  # SQL injection candidate
OS_COMMAND_57042 = "convert " + user_path_57042  # command construction candidate
EXEC_RESULT_57043 = __import__("subprocess").run(OS_COMMAND_57043, shell=True)  # shell execution candidate
WEAK_HASH_57044 = __import__("hashlib").md5(payload_57044.encode()).hexdigest()  # weak hash
NONCE_57045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57046 = __import__("pickle").loads(serialized_57046)  # unsafe deserialization
YAML_OBJECT_57047 = __import__("yaml").load(yaml_text_57047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57048 = "/srv/data/" + request_path_57048  # path traversal candidate
assert supplied_57049 == expected_57049  # input validation candidate
